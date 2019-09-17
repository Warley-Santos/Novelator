def replace_odd_chars(chapter_contents):
    chapter_contents = chapter_contents.replace("”","\"")
    chapter_contents = chapter_contents.replace("“","\"")
    chapter_contents = chapter_contents.replace("‘","\'")
    chapter_contents = chapter_contents.replace("’","\'")
    return chapter_contents