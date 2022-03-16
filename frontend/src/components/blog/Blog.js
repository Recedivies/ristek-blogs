import React, { useEffect, useState } from "react";
import blogService from "../../services/blog";
import { meService } from "../../services/me";
import { toast } from "react-toastify";
import BlogForm from "./BlogForm";

const Blog = () => {
  const isAuthenticated = localStorage.getItem("token") !== null;
  const [blogs, setBlogs] = useState([]);
  const [me, setMe] = useState({});

  useEffect(async () => {
    try {
      const blogsData = await blogService.listBlog();
      if (isAuthenticated) {
        const meData = await meService();
        setMe(meData);
      }
      setBlogs(blogsData.data);
    } catch (err) {
      if (err.response) console.log(err.response);
      toast.error(
        `${JSON.stringify(err.response.data.detail)} (${err.response.status})`
      );
    }
  }, []);

  if (blogs.length === 0) {
    return <div>No blogs</div>;
  }

  return (
    <div>
      <h1>Blog</h1>

      {blogs.length !== 0 &&
        blogs.map((blog) => {
          return (
            <div key={blog.title}>
              <h1>{blog.title}</h1>
              <div>{blog.body}</div>
              <div>created at {blog.created_at}</div>
            </div>
          );
        })}

      {me.is_staff === true && isAuthenticated && <BlogForm />}
    </div>
  );
};

export default Blog;
