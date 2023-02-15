import openai
import streamlit as st
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
    st.title("ChatGPT")
    st.write("请提问:")

    # 获取用户输入
    prompt = st.text_input("", "")

    if prompt:
        # 获取回答
        answer = get_answer(prompt)

        # 显示回答
        st.write("回答：")
        st.write(answer)

'''
        # 保存回答到本地文件
        save_answer = st.button("保存回答")
        if save_answer:
            with open("answer.txt", "w") as file:
                file.write(answer)
            st.write("回答已保存。")
'''
if __name__ == "__main__":
    main()
