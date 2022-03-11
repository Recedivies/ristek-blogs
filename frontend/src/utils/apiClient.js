import axios from "axios";

const apiClient = axios.create({
  url:
    "https://cors-anywhere.herokuapp.com/" + process.env.REACT_APP_BACKEND_URL,
});

export default apiClient;
