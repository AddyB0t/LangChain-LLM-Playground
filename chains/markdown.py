from langchain.text_splitter import RecursiveCharacterTextSplitter


text="""# My Document

## Introduction

This is a sample markdown document that demonstrates different header levels.

## Main Content

### Section 1

This is the content of section 1. It contains some important information.

### Section 2

This section covers another topic with details and examples.

## Conclusion

To summarize the key points from this document:
- Markdown is easy to use
- Headers help organize content
- The MarkdownHeaderTextSplitter can process this structure
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)

result=splitter.split_text(text)

print(result)
