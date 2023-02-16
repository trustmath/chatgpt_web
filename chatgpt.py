import openai
import streamlit as st
from PIL import Image
import os

# 设置OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


# 获取回答
def get_answer(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    answer = response.choices[0].text
    return answer

# 创建Streamlit App
def main():
    st.title("ChatGPT，用人工智能点亮你的灵感火花，创造无限可能！")
    st.write("请提问:")

    # 创建输入框和提交按钮
    user_input = st.text_input("", "")
    submit_button = st.button("提交")

    # 判断用户是否点击了提交按钮
    if submit_button or user_input:

        # 获取回答
        answer = get_answer(user_input)

        # 显示问题和回答
        st.write("问题：",user_input)
        st.write("回答：",answer)



    
    #网站介绍
    #st.write("非常感谢您访问我们的网站！我们很高兴地告诉您，我们已经为您实现了在国内直接访问 ChatGPT 的功能，让您可以在本地便捷地进行提问和回答。我们希望您可以在这里得到您所需要的帮助和信息。")
    #st.write("我们为了提供更好的服务和更稳定的用户体验，需要您的支持和帮助。如果您认为我们的网站帮助了您，我们希望您可以考虑付费支持我们，这将有助于我们更好地维护和改进我们的服务。感谢您对我们的支持！")
    #显示微信赞赏码
    image = Image.open("wechat-reward-code.jpg")
    st.image(image, caption="微信赞赏码", use_column_width=True)


if __name__ == "__main__":
    main()
