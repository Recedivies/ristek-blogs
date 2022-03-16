import AxiosClient from "./apiClient";
const baseUrl = "/api/users/me/";

export const meService = async () => {
  const response = await AxiosClient.get(baseUrl);
  return response.data;
};
