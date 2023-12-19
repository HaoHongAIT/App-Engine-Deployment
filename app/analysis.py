import openai


class Analysis:
    def __init__(self, api_key, model="text-davinci-003"):
        self.model = model
        openai.api_key = api_key  # https://platform.openai.com/api-keys

    def get_response(self, news):
        prompt = f"""hãy phân tích bài báo sau một cách ngắn gọn :"
        {news}"
        """
        response = openai.Completion.create(engine=self.model,
                                            prompt=prompt,
                                            max_tokens=1024,
                                            n=1, temperature=0.5)
        return response.choices[0].text


# if __name__ == '__main__':
#     model = Analysis()
#     user_question = "xin chào "
#     response_text = model.get_response(user_question)
#     print(response_text)
