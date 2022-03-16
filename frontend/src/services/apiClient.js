import axios from "axios";

const apiClient = axios.create({
  url:
    "https://cors-anywhere.herokuapp.com/" + process.env.REACT_APP_BACKEND_URL,
  headers: { "Content-Type": "application/json" },
});

// before sending request attach auth token
apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  config.headers.Authorization = token ? `Bearer ${token}` : "";
  return config;
});

export default apiClient;
