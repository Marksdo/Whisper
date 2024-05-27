# Translate using chatGPT
it also can use other llm model (use litellm to proxy it to chatGPT formate)
https://github.com/BerriAI/litellm

## Use template to ask gpt

![gpt0](gpt0.png)

## instructions also support use template replace vars

![gpt1](gpt1.png)

example instructions code, you can use your language to set the prompt

```
You are an expert in English-Korean translation and need to translate a text that has been transcribed from speech. I will provide you with the full transcription for reference. Please provide better adaptability in translating the information based on the content of the full transcription. You only need to reply with the translated content. 
Here is the full transcription:

{%- for st in subtitles %}
{{ st.text }}
{% endfor %}

```

you can use your language to custom the gpt instructions and templates

## Use in subtitle editor

![gpt-editor](gpt-editor.png)


## instructions & template script examples
it use the sample template engine use in custom export template feature, so more vars can found in template config

![gpt-template](gpt-template.png)

### loop subtitle
```
{%- for st in subtitles -%}
{{ st.text }}
{% endfor %}
```

### current active subtitle row origin text
```
{{ st.text }}
```

...

## Test gpt 

![gpt-test](gpt-test.png)

@todo finish test description