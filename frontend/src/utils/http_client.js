import axios from 'axios';

const http = axios.create({
  baseURL: 'http://localhost:5000',
  timeout: 5000,
});

http.interceptors.request.use(
  (config) => config,
  (error) => Promise.reject(error),
);

http.interceptors.response.use(
  (response) => response,
  (error) => Promise.reject(error),
);

export default http;
