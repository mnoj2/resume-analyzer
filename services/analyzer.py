import re

def extract_name(content):
    lines = content.split('\n')
    for line in lines:
        clean_line = line.strip()
        if clean_line:
            return clean_line
    return "Name Not Found"

def get_matched(content, req_data):
    matched_data = []
    for data in req_data:
        pattern = rf"\b{re.escape(data)}\b"
        if re.search(pattern, content, re.IGNORECASE):
            matched_data.append(data)
    return matched_data

def analyze_resume(content, req_skills, req_locations):

    matched_skills = get_matched(content, req_skills)
    locations = get_matched(content, req_locations)
    candidate_name = extract_name(content)

    score = (len(matched_skills) / len(req_skills) * 100)

    warnings = []
    if len(content.split()) < 30:
        warnings.append("Resume is too short (< 30 words)")
    if not matched_skills:
        warnings.append("No skills matched")
    if not locations:
        warnings.append("No location detected")

    response = {
        "candidate_name": candidate_name,
        "word_count": len(content.split()),
        "matched_skills": matched_skills,
        "match_score": round(score, 2),
        "entities": {
            "locations": locations
        },
        "warnings": warnings
    }
    if not warnings:
        response['message'] = 'Resume is proper'

    return response