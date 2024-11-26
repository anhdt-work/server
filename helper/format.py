def format_response_as_html(raw_text: str) -> str:
    # Example transformation for code blocks and text
    raw_text = raw_text.replace("\r", "")
    print(raw_text)
    lines = raw_text.split("\n")
    inside_code_block = False
    formatted_lines = []
    for line in lines:
        if line.startswith("```"):  # Code block marker
            if inside_code_block:
                formatted_lines.append("</code></pre>")
                inside_code_block = False
            else:
                formatted_lines.append("<pre><code>")
                inside_code_block = True
        else:
            formatted_lines.append(f"<p>{line}</p>")
    rs = "".join(formatted_lines)
    print(rs)
    return rs