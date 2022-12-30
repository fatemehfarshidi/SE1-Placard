import { useState, useContext } from "react";
import AuthContext from "../context/AuthContext";
import "./auth.css";

function Register() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [password2, setPassword2] = useState("");
  const { registerUser } = useContext(AuthContext);

  const handleSubmit = async e => {
    e.preventDefault();
    registerUser(username, password, password2);
  };

  return(
      <div className="auth-form-container">
        {/* the svg designs */}
        <div className="light-blub">
          <svg width="384" height="206" viewBox="0 0 384 206" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M204.731 1.2171C268.802 7.03621 329.998 42.3149 363.703 97.0908C395.981 149.547 380.945 213.504 372.923 274.556C364.313 340.089 372.901 422.332 316.448 456.747C260.437 490.893 195.001 432.928 130.219 422.516C63.324 411.764 -22.9651 449.99 -63.4555 395.688C-103.928 341.411 -54.9158 266.921 -33.7384 202.632C-16.8686 151.42 3.25533 102.895 44.4566 68.0957C90.4245 29.2705 144.789 -4.22708 204.731 1.2171Z" fill="#E3E8C0"/>
          </svg>
        </div>
        <div className="green-blub">
          <svg width="672" height="667" viewBox="0 0 672 667" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M960.756 293.016C998.781 397.683 917.42 498.262 896.31 607.475C877.655 703.987 921.359 823.693 846.011 886.659C770.018 950.163 658.929 883 559.974 888.536C412.267 896.799 253.314 1015.31 134.769 926.447C11.0027 833.667 -35.7687 631.333 31.4075 492.3C94.9422 360.803 305.378 421.55 421.471 333.065C536.755 245.197 531.327 11.7556 675.986 1.01276C816.702 -9.43728 912.504 160.198 960.756 293.016Z" fill="#008080"/>
          </svg>
        </div>
        <div className="orange-blub">
          <svg width="511" height="335" viewBox="0 0 511 335" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M-27.1815 -293.202C39.9494 -320.198 106.582 -347.538 176.003 -351.922C252.071 -356.726 329.771 -352.802 385.83 -319.283C443.717 -284.671 470.532 -225.511 488.043 -165.345C506.207 -102.937 527.628 -33.4741 487.983 31.7038C448.905 95.9482 352.564 118.771 285.853 167.063C219.43 215.145 175.796 287.741 97.0943 314.66C13.4756 343.261 -75.1559 337.905 -149.945 316.124C-226.024 293.967 -303.719 257.493 -324.565 191.859C-344.889 127.872 -274.023 55.4749 -255.177 -15.1977C-239.15 -75.3 -266.431 -137.91 -222.267 -191.761C-177.96 -245.786 -96.6962 -265.247 -27.1815 -293.202Z" fill="#EE7B30"/>
          </svg>
        </div>
        {/* the logo in header */}
        <div className="header-logo">
          <svg width="64" height="64" viewBox="0 0 87 87" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M1 1H86V44.9651H1V1Z" stroke="black" stroke-width="2" stroke-miterlimit="10" stroke-linejoin="round"/>
            <path d="M39.5018 45.1752H47.4735V85.9999H39.5018V45.1752Z" stroke="black" stroke-width="2" stroke-miterlimit="10" stroke-linejoin="round"/>
            <path d="M8.1301 7.92542H78.8969V38.1984H8.1301V7.92542Z" stroke="black" stroke-width="2" stroke-miterlimit="10" stroke-linejoin="round"/>
            <path d="M78.4718 26.5582H66.2081" stroke="black" stroke-width="2" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M66.1492 8.18945V37.6538" stroke="black" stroke-width="2" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M53.7675 8.56104L53.8855 37.3885L53.7675 8.56104Z" fill="black"/>
            <path d="M53.7675 8.56104L53.8855 37.3885" stroke="black" stroke-width="2" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M45.2423 15.6947L45.3329 34.0473" stroke="black" stroke-width="2" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M45.2423 19.5375L45.3329 37.8903" stroke="black" stroke-width="2" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M45.3045 15.3934L65.7139 8.43066" stroke="black" stroke-width="2" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M33.6309 15.9613L33.9059 37.4211" stroke="black" stroke-width="2" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M26.679 23.5443L26.7706 38.0709" stroke="black" stroke-width="2" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M29.1472 38.1964H20.7109" stroke="black" stroke-width="2" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M12.6756 26.7872H20.6393" stroke="black" stroke-width="2" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M12.4528 34.4675H20.6152" stroke="black" stroke-width="2" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M20.6442 26.8104V34.4716" stroke="black" stroke-width="2" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M70.123 30.3558L74.2544 30.356L70.123 30.3558Z" fill="black"/>
            <path d="M70.123 30.3558L74.2544 30.356" stroke="black" stroke-width="2" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M72.3229 32.8382L72.3228 32.8381" stroke="black" stroke-width="2" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        {/* Register Form */}
        <form className="main-form" onSubmit={handleSubmit}>

          {/* Other related texts & links */}
          <div className="header-text">
            <h5>به پلاکارد خوش آمدید</h5>
            {/*<div className="left-header">*/}
            {/*  <h5>حساب کاربری دارید؟</h5>*/}
            {/*  <button id='btn1' onClick={()=>props.onFormSwitch('Login')}>وارد شوید</button>*/}
            {/*</div>*/}
          </div>

          {/* the login part */}
          <div className='text-part'>
            <h1>ثبت نام</h1>

            <label htmlFor="email">نام کاربری خود را وارد کنید</label>
            <input value={username} onChange={(e) => setUsername(e.target.value)} type='text' id='username' placeholder= "  John-Doe" />

            <label htmlFor="password">رمزعبور خود را وارد کنید</label>
            <input value={password} onChange={(e) => setPassword(e.target.value)} type='password' id='password' placeholder="  ********" />

            <label htmlFor="password">رمزعبور خود را تکرار کنید</label>
            <input value={password2} onChange={(e) => setPassword2(e.target.value)} type='password' id='confirm-password' placeholder="  ********" />

            <button id= "btn2" type="submit">ثبت نام</button>

          </div>
        </form>
      </div>
  )
}

export default Register;
