import AxiosClient from "./apiClient";
const baseUrl = "/api/blogs/";

const listBlog = async () => {
  return await AxiosClient.get(baseUrl);
};
const createBlog = async (data) => {
  const response = await AxiosClient.post(baseUrl, data);
  return response.data;
};

const blogService = { listBlog, createBlog };

export default blogService;
