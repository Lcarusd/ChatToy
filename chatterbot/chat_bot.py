# coding: utf-8

# from botbase import ChatBotBase
# import requests
# bot_api = "http://127.0.0.1:8000/get_response"
#
#
# class ChatBot(ChatBotBase):
#     def handle_msg_all(self, msg):
#         if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
#             user_input = msg["content"]["data"]
#             payload = {"user_input": user_input}
#             response = requests.get(bot_api, params=payload).json()["response"]
#             self.send_msg_by_uid(response, msg['user']['id'])
#
#
# def main():
#     bot = ChatBot()
#     bot.DEBUG = True
#     bot.conf['qr'] = 'png'
#     bot.run()
#
#
# if __name__ == '__main__':
#     main()
