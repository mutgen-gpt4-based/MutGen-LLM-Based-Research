USER_PROMPT = """
<code_snippet_one>
```java
{fixed_code}
```
</code_snippet_one>

<code_snippet_two>
```java
{buggy_code}
```
</code_snippet_two>

Provide me a list with all modifications to transform code snippet one into code snippet two.
    """