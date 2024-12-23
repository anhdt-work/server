def format_response_as_html(raw_text: str) -> str:
    raw_text = raw_text.replace("\r", "")
    lines = raw_text.split("\n")
    inside_code_block = False
    formatted_lines = []
    for line in lines:
        if "```" in line:  # Code block marker
            if inside_code_block:
                formatted_lines.append("</code></pre>")
                inside_code_block = False
            else:
                formatted_lines.append("<pre><code>")
                inside_code_block = True
        else:
            formatted_lines.append(f"<div>{line}</div>")
    rs = "".join(formatted_lines)
    return rs
