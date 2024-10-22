# Here created a Google - Clone design using Streamlit
# In streamlit you can use html and css 

import streamlit as st

def main():
    # Styling using Streamlit markdown
    st.markdown(
        """
        <style>
            html {
                height: 100%;
                font-size: 100%;
            }
            
            body {
                font: 13px arial, sans-serif;
            }
            


                nav {
                display: flex;
                justify-content: flex-end;
                align-items: center;
                padding: 10px;
                background-color: #ffffff;
                float: right;
                margin-right: -44%;
                margin-top: -6%;
            }

            .right_nav {
                list-style: none;
                display: flex;
                align-items: center;
                gap: 20px;
                margin: 3rem;
            }

            .apps {
                width: 16px;
                height: 16px;
                opacity: 0.75;
                transition: opacity 0.2s;
            }

            .apps:hover {
                opacity: 1;
            }

            .sign_in {
                height: 60%;
                background: #4285f4;
                width: 86px;
                height: 35px;
            }

            .sign_in a {
                font-weight: bold;
                color: #fff;
                text-decoration: none;
                padding-left: 10%;
            }

            .sign_in a:hover {
                text-decoration: none;
            }
              
            .cntr_pg {
                position: absolute;
                top: 40%;
                left: 50%;
                margin-right: -40%;
                transform: translate(-50%, -50%);
                margin: 3rem;
            }
            
            .logo {
                display: block;
                margin: auto;
                height: 92px;
                width: 272px;
                margin-top:40%;
            }
            
            .search_bar {
                border-radius: 40px;
                width: 585px;
                margin: auto;
                height: 39px;
                border: .7px solid #E4E4E4;
                background-color: #fff;
                box-shadow: 0px 1px 4px #E4E4E4;
                margin-bottom: 20px;
                outline: none;
                text-indent: 15px;
            }
            
            .search_bar:hover, .search_bar:active {
                padding-bottom: 2px;
                padding-top: 1px;
                margin-top: -1px;
                width: 585px;
                box-shadow: 0px 3px 8px #E4E4E4;
                outline: none;
            }
            
            .mic {
                width: 14px;
                height: 20px;
                position: relative;
                left: 555px;
                top: 34px;
            }
            
            .submit_buttons {
                display: inline-block;
                height: 36px;
                cursor: pointer;
                line-height: 27px;
                background-color: #f2f2f2;
                border: 1px solid #f2f2f2;
                border-radius: 2px;
                color: #757575;
                cursor: default;
                font-family: arial, sans-serif;
                font-size: 13px;
                font-weight: bold;
                margin: 11px 4px;
                min-width: 54px;
                padding: 0 16px;
                text-align: center;
            }
            
            .submit_buttons {
                position: relative;
                left: 25%;
                right: -50%;
                cursor: pointer;
            }
            
            .submit_buttons:hover {
                border: .7px solid #d0d0d0;
                color: #000;
                box-shadow: 0px 1px 4px #E4E4E4;
            }
            
           
        </style>
        """,
        unsafe_allow_html=True
    )



  # Navigation (navbar)
    st.markdown(
        """
        <nav>
            <ul class="right_nav">
                <li><a href="#" style="color: black;">Gmail</a></li>
                <li><a href="#" style="color: black;">Images</a></li>
                <li><a href="#"><img class="apps" src="https://thumb.ibb.co/gykLCw/grid_menu.png"></a></li>
                <li class="sign_in" style="padding: 2%; margin-left: 2%"><a href="#">Sign in</a></li>
            </ul>
        </nav>
        """,
        unsafe_allow_html=True
    )

    # Center content
    st.markdown(
        """
        <section class="cntr_pg">
              <img class="logo" src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png" alt="Google logo" />
             <img class="mic" src="https://upload.wikimedia.org/wikipedia/commons/2/22/Google_microphone_logo.png" alt="" />
            <form action="#" method="#" name="searchquery" class="form">
                <input type="text" name="searchfield" class="search_bar">
                <div class="search_buttons">
                        <input class="submit_buttons" type="submit" value="Google Search" name="submit">
                    <input class="submit_buttons" type="submit" value="I'm Feeling Lucky" name="feelinglucky">
                   </div>
            </form>
        </section>
        """,
        unsafe_allow_html=True
    )

   

if __name__ == "__main__":
    main()