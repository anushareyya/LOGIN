import React, { useState } from "react";

const LoginForm = () => {
  const [username, setUsername] = useState();
  const [password, setPassword] = useState();
  const [note,setNote]=useState("Enter Username and Password");
  const [alert,setAlert]=useState("note");
  

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle login logic here
    if (username === "karthik") {
      setNote('logged In')
      setAlert('alert alert-success')
    }
    else{
      setNote("invalid username and pasword");
      setAlert("alert alert-danger");
    }
  };

  return (
    <div id="login-Form">
      <div id="form">
        <h2>Login</h2>
        <form onSubmit={handleSubmit}>
          <div className={alert} style={{display:'flex'}}>{note}</div>
          <div>
            <label>Username:</label>
            <input
              type="text"
              value={username}
              onChange={(e) => {setUsername(e.target.value)
              console.log(e.target.value)}}
              required
            />
          </div>
          <div>
            <label>Password:</label>
            <input
              type="password"
              value={password}
              onChange={(e) => {setPassword(e.target.value)
                console.log(e.target.value)}}
              required
            />
          </div>
          <button type="submit">Login</button>
        </form>
      </div>
    </div>
  );
};

export default LoginForm;
