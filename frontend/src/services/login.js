import AxiosClient from "./apiClient";
const baseUrl = "/api/login/";

export const loginService = async (credentials) => {
  const response = await AxiosClient.post(baseUrl, credentials);
  return response.data;
};
