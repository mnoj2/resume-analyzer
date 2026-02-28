def validate_and_read_file(file):
    if not file or file.filename == "":
        return None, "No file selected", 400

    if not file.filename.lower().endswith(".txt"):
        return None, "Only .txt files allowed", 400

    try:
        content = file.read().decode("utf-8")
        clean_content = " ".join(content.split())

        if not clean_content:
            return None, "The uploaded file is empty", 400

        return content, None, None

    except UnicodeDecodeError:
        return None, "File is not a valid UTF-8 text file", 400

    except Exception:
        return None, "Server error while reading file", 500