import React, { useState } from "react";
import {
  Button,
  Container,
  Grid,
  Link,
  Avatar,
  Typography,
  TextField,
} from "@mui/material";

import LockOpenOutlinedIcon from "@mui/icons-material/LockOpenOutlined";
import { loginService } from "../../services/login";
import { useNavigate } from "react-router";
import { onSubmit, submitWithEnter } from "../../utils/forms";
import { toast } from "react-toastify";

const Login = () => {
  const navigate = useNavigate();

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const submitForm = async () => {
    try {
      const data = await loginService({
        username: username,
        password: password,
      });
      localStorage.setItem("token", data.access);
      localStorage.setItem("refresh_token", data.refresh);
      toast.success("Logged in! Redirecting to home page ...");
      setTimeout(() => {
        navigate("/");
        window.location.reload();
      }, 2000);
    } catch (err) {
      if (err.response) console.log(err.response);
      toast.error(
        `${JSON.stringify(err.response.data.detail)} (${err.response.status})`
      );
    }
  };

  const handleChange = (e) => {
    switch (e.target.id) {
      case "username":
        setUsername(e.target.value);
        break;
      case "password":
        setPassword(e.target.value);
        break;
      default:
        break;
    }
  };

  const onEnterKeyDown = (e) => submitWithEnter(e, submitForm);

  return (
    <Container component="main" maxWidth="xs">
      <div className="auth">
        <Avatar className="auth-icon">
          <LockOpenOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Sign in
        </Typography>
        <form noValidate onSubmit={(e) => onSubmit(e, submitForm)}>
          <div className="auth-form">
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              id="username"
              label="User Name"
              name="username"
              autoFocus
              onChange={handleChange}
            />
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              name="password"
              label="Password"
              type="password"
              id="password"
              autoComplete="current-password"
              onChange={handleChange}
              onKeyDown={onEnterKeyDown}
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className="auth-button"
              onKeyDown={onEnterKeyDown}
            >
              Sign In
            </Button>
            <Grid container justifyContent="flex-end">
              <Grid item>
                <Link href="/signup/" variant="body2">
                  {" Don't have an account? Sign Up "}
                </Link>
              </Grid>
            </Grid>
          </div>
        </form>
      </div>
    </Container>
  );
};

export default Login;
