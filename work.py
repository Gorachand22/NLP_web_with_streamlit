"""All the processing code goes here."""
import streamlit as st
import json
import paralleldots as para

class Database:
    def signup(self):
        name = st.text_input("Enter your name")
        email = st.text_input("Enter your email")
        password = st.text_input("Enter your password", type="password")
        if st.button("Sign Up") and name and email and password:
            if email.endswith('@gmail.com') and len(password) >=6:
                if self.check_signup(email):
                    self.insert(email, password, name)
                    st.success("You have successfully created an account")
                    st.info("Go to Log in page to login")
                else:
                    st.error("Email already exists")
            else:
                st.error("Invalid email or password")
    
    def check_signup(self, email):
        """Check if the email exists in the user.json file"""
        val = None
        with open("user.json", "r") as file:
            data = json.load(file)
            if email in data.keys():
                val = False
            else:
                val = True
        return val

    def insert(self, email, password, name):
        """Insert the data into the user.json file"""
        with open("user.json", "r") as file:
            data = json.load(file)
        
        data[email] = [password, name]
        
        with open("user.json", "w") as file:
            json.dump(data, file, indent=4)
            

    def check_login(self):
        email = st.text_input("Enter your Current email")
        password = st.text_input("Enter your Current password", type="password")
        if st.button("Log in") and email and password:
            with open("user.json", "r") as file:
                data = json.load(file)
                if email in data.keys() and data[email][0] == password:
                    st.success("You have successfully logged in")
                    st.session_state['is_api'] = True
                else:
                    st.error("Invalid email or password")
                    st.session_state['forget_pass'] = True
    
    def forget_password(self):
            st.sidebar.info("Forget Password?")
            current_mail = st.sidebar.text_input("Enter your email")
            new_password = st.sidebar.text_input("Enter your new password", type="password")
            confirm_password = st.sidebar.text_input("Enter your confirm password", type="password")
            if st.sidebar.button("Change Password") and current_mail and new_password and confirm_password:
                if new_password == confirm_password:
                    with open("user.json", "r") as file:
                        data = json.load(file)
                        if current_mail in data.keys():
                            data[current_mail][0] = new_password
                            with open("user.json", "w") as file:
                                json.dump(data, file, indent=4)
                                st.sidebar.success("Password changed successfully")
                                st.session_state['forget_pass'] = False
                        else:
                            st.sidebar.error("Invalid email")
                else:
                    st.sidebar.error("Passwords do not match")
    
    def API(self):
        st.markdown("https://dashboard.komprehend.io/resources")
        my_api_key = st.text_input("Enter your API key", type="password")
        if st.button("Submit") and my_api_key:
            if len(my_api_key) == 43:
                st.session_state['api_key'] = my_api_key
                para.set_api_key(st.session_state['api_key'])
                st.success('Valid API Key')
                st.session_state['is_api'] = False
                st.balloons()
            else:
                st.error('Invalid API Key')


class API:
    def ner_analysis(self, text):
            response = para.batch_ner([text])
            for entity in response['entities']:
                st.write(f"name ==> { entity[0]['name']} , category ==> { entity[0]['category']}")
            
    def check_abuse(self, text):
            response = para.batch_abuse([text])
            d = response['abuse'][0]
            ans = sorted(d, key = lambda x: d[x], reverse=True)[0]
            st.write(ans)