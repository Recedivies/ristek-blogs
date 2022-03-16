import React, { useState } from "react";
import {
  Button,
  TextField,
  Link,
  Grid,
  Typography,
  Container,
  Avatar,
} from "@mui/material";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";

import { signupService } from "../../services/signup";
import { useNavigate } from "react-router";
import { toast } from "react-toastify";
import { onSubmit, submitWithEnter } from "../../utils/forms";

const validateUsername = (email) => {
  return 8 <= email.length && email.length <= 32;
};

const Signup = () => {
  const navigate = useNavigate();

  const [username, setUsername] = useState("");
  const [fullName, setFullName] = useState("");
  const [password1, setPassword1] = useState("");
  const [password2, setPassword2] = useState("");

  const submitForm = async () => {
    try {
      await signupService({
        username: username,
        full_name: fullName,
        password: password1,
        password2: password2,
      });
      toast.success("Created account! Redirecting to login page...");
      setTimeout(() => navigate("/login"), 1000);
    } catch (err) {
      if (err.response)
        toast.error({
          message: `${err.response.statusText} (${err.response.status})`,
          severity: "error",
        });
    }
  };

  const passwordsMatch = () => password1 === password2;

  const onEnterKeyDown = (e) => submitWithEnter(e, submitForm);

  return (
    <Container component="main" maxWidth="xs">
      <div className="auth">
        <Avatar className="auth-icon">
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Sign up
        </Typography>
        <form
          className="auth-form"
          noValidate
          onSubmit={(e) => onSubmit(e, submitForm)}
        >
          <Grid container spacing={2}>
            <Grid item xs={12}>
              <TextField
                autoComplete="uname"
                name="User Name"
                variant="outlined"
                required
                fullWidth
                id="username"
                label="User Name"
                autoFocus
                onChange={(e) => setUsername(e.target.value)}
                error={username !== "" && !validateUsername(username)}
                onKeyDown={onEnterKeyDown}
                helperText={
                  username !== "" &&
                  !validateUsername(username) &&
                  "It must contain at least 8 character."
                }
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="FullName"
                label="FullName"
                name="FullName"
                autoComplete="FullName"
                type="FullName"
                onChange={(e) => setFullName(e.target.value)}
                onKeyDown={onEnterKeyDown}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                name="password"
                label="Password"
                type="password"
                id="password1"
                autoComplete="current-password"
                onChange={(e) => setPassword1(e.target.value)}
                error={!passwordsMatch()}
                helperText={!passwordsMatch() && "Passwords don't match"}
                onKeyDown={onEnterKeyDown}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                name="password2"
                label="Confirm password"
                type="password"
                id="password2"
                autoComplete="current-password"
                onChange={(e) => setPassword2(e.target.value)}
                error={!passwordsMatch()}
                helperText={!passwordsMatch() && "Passwords don't match"}
                onKeyDown={onEnterKeyDown}
              />
            </Grid>
          </Grid>
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className="auth-button"
          >
            Sign Up
          </Button>
          <Grid container justifyContent="flex-end">
            <Grid item>
              <Link href="/login/" variant="body2">
                Already have an account? Sign in
              </Link>
            </Grid>
          </Grid>
        </form>
      </div>
    </Container>
  );
};

export default Signup;
