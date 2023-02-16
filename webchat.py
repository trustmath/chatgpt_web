import openai
import streamlit as st

# 设置OpenAI API key
openai.api_key = "YOUR_API_KEY"

# 获取回答
def get_answer(prompt):
    response = openai.Completion.create(
        engine="davinci",
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

    # 创建输入框和提交按钮
    user_input = st.text_input("", "")
    submit_button = st.button("提交")

    # 判断用户是否点击了提交按钮
    if submit_button and user_input:
        # 禁用提交按钮，以避免重复提交
        submit_button = submit_button
        submit_button.empty()
        submit_button = submit_button.button("提交中...", key="submit_button", disabled=True)

        # 获取回答
        answer = get_answer(user_input)

        # 显示回答
        st.write("回答：")
        st.write(answer)

        # 创建保存回答按钮
        save_answer = st.button("保存回答")

        # 判断用户是否点击了保存回答按钮
        if save_answer:
            # 弹出对话框，让用户选择保存路径
            save_path = st.text_input("请输入保存路径", "answer.txt")

            # 保存回答到本地文件
            with open(save_path, "w") as file:
                file.write(answer)
            st.write("回答已保存。")

        # 启用提交按钮，以允许下一次提交
        submit_button.empty()
        submit_button = submit_button.button("提交", key="submit_button")

if __name__ == "__main__":
    main()
