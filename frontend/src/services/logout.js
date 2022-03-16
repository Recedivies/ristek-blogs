import AxiosClient from "./apiClient";
const baseUrl = "/api/logout/";
import { toast } from "react-toastify";

export const onLogout = async () => {
  return await AxiosClient.delete(baseUrl);
};

export const logout = async () => {
  try {
    await onLogout();
    localStorage.removeItem("token");
    toast.success("Logged out!");
    setTimeout(() => {
      window.location.reload();
    }, 2000);
  } catch (err) {
    return console.log(err);
  }
};
