__author__ = 'Vyasraj Vaidya'

# assignement from Plivo
# Scenarios :
# 1. Use any two numbers listed in the account for sending message. use message api to send an sms from a number to another number.
# 2. Once message api is successful, response give message uuid.Using this message uuid get the details of the message using details api.
# 3. Use pricing api to determine the rate of the message which is outbound rate under message object in this case.
# 4. Verify the rate and the price deducted for the sending message, should be same.
# 5. And finally after sending message, using account details api, account cash credit should be less than by the deducted amount.

import plivo, json, xml

class messageScenarios():
    def __init__(self):
        self.auth_id = 'SAZGJJMTQ5NMVJODK4NM'
        self.auth_token = 'ZWMxYzg2NDliYjIyODkwMGNkNzc4MzQxMzFjODhl'

    def comMsg(self):
        p = plivo.RestAPI(self.auth_id, self.auth_token)
        try:
            response = p.Message.create(
            src='+13238318440',
            dst='+13252210570',
            text='Test Message',)
            print(response)
        except plivo.PlivoError as e:
            print(e)

    def getResponse(self):
        # Message Detail Record i.e. MDR has several attributes
        p = plivo.RestAPI(self.auth_id, self.auth_token)  # ??
        try:
            xml_response = plivo.XML.Response()  # missing argument
            print ("Response:{}".format(xml_response))
        except plivo.PlivoError as e:
            print(e)

    def getMsgRate(self):
        try:
            msgRate = plivo.Message()
            print("Message Rate:{}".format(msgRate))
        except plivo.PlivoError as e:
            print(e)

    def getMsgPrice(self):
        try:
            msgPrice = plivo.Pricing()
            print("Message Price:{}".format(msgPrice))
        except plivo.PlivoError as e:
            print (e)

    def getAccDetails(self):
        try:
            p = plivo.RestAPI(self.auth_id, self.auth_token)
            accDets = plivo.Account()
            print("Account Details:{}".format(accDets))
        except plivo.PlivoError as e:
            print (e)

    def process(self):
        print("Currrent Account Details:")
        currentAccDetails = self.getAccDetails()
        print("send text message")
        self.comMsg()
        print("response:")
        self.getResponse()
        print("Rate of message:")
        self.getMsgRate()
        print("message price:")
        self.getMsgPrice()
        print("New Account Details:")
        newAccDetails = self.getAccDetails()


if __name__ == "__main__":
    c = messageScenarios()
    c.process()
