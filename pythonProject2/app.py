# agent.py
from openai import OpenAI

client = OpenAI(api_key="你的API_KEY")

def analyze_text(text):
    prompt = f"""
    你是一个AI分析助手，请完成以下任务：
    1. 总结文本
    2. 提取关键词
    3. 给出结论

    文本：
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content