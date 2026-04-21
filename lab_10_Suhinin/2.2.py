def make_html_tag(tag_name, content, **attributes):
    attrs = []

    for key, value in attributes.items():
        if key.endswith('_'):  # для class_
            key = key[:-1]
        attrs.append(f'{key}="{value}"')

    attr_string = " ".join(attrs)

    if attr_string:
        return f"<{tag_name} {attr_string}>{content}</{tag_name}>"
    else:
        return f"<{tag_name}>{content}</{tag_name}>"
print(make_html_tag("p", "Hello World"))