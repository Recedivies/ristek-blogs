import { toast } from "react-toastify";
import {
  CREATE_USER_ERROR,
  CREATE_USER_SUBMITTED,
  CREATE_USER_SUCCESS,
} from "./SignupTypes";

import { signupService } from "../../services/signup";
import { useNavigate } from "react-router-dom";

export const signupNewUser = (userData) => (dispatch) => {
  const navigate = useNavigate();

  dispatch({ type: CREATE_USER_SUBMITTED }); // set submitted state
  signupService(userData)
    .then(() => {
      toast.success({
        message: "Created account! Redirecting to login page...",
        severity: "success",
      });
      dispatch({ type: CREATE_USER_SUCCESS });
      setTimeout(() => navigate.push("/login"), 1000);
    })
    .catch((err) => {
      if (err.response) {
        toast.error({
          message: `${err.response.statusText} (${err.response.status})`,
          severity: "error",
        });
        dispatch({
          type: CREATE_USER_ERROR,
          errorData: error.response.data,
        });
      } else if (error.message) {
        toast.error(JSON.stringify(error.message));
      } else {
        toast.error(JSON.stringify(error));
      }
    });
};
