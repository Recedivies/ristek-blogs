import AxiosClient from "./apiClient";
const baseUrl = "/api/posts/";

const createPost = async (data) => {
  const response = await AxiosClient.post(baseUrl, data);
  return response.data;
};

const updatePost = async (data) => {
  const response = await AxiosClient.put(baseUrl, data);
  return response.data;
};

const deletePost = async (data) => {
  const response = await AxiosClient.delete(baseUrl, data);
  return response.data;
};

const postService = { createPost, updatePost, deletePost };

export default postService;
