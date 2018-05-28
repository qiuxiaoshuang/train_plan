import json
def sign_up():#注册函数
    usersname={}
    usename=input("请输入一个用户名:\n")
    password=input("请输入密码:\n")
    usersname[usename]=password
    filename='username.json'
    with open(filename,'a') as f_obj:
        json.dump(usersname,f_obj)
        return usersname



def sign_in(name,passw):
    filename='username.json'
    with open(filename) as f_obj:
        usersname=json.load(f_obj)
        if usersname.has_key(name) is True:
            if usersname[name]==passw:
                print("登录成功")
                flag=True
            else:
                print("密码错误")
                flag=False
        else:
            print("无该用户，请注册")
            usersname=sign_up()
   # return(flag)

def main():
    name=input("请输入用户名:\n")
    password=input("请输入密码:\n")
    sign_in(name,password)
    # sign_up()


main()