import AxiosClient from "./apiClient";
const baseUrl = "/api/users/";

export const signupService = async (credentials) => {
  const response = await AxiosClient.post(baseUrl, credentials);
  return response.data;
};
