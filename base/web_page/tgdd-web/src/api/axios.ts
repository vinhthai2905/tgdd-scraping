import axios from 'axios'

const axiosInstance = axios.create({
  baseURL: '', // relative to current origin
  headers: {
    'Content-Type': 'application/json',
  },
})


export const get = async <T>(
  url: string,
  config?: AxiosRequestConfig
): Promise<T> => {
  try {
    const response: AxiosResponse<T> = await axiosInstance.get(url, config);
    return response.data;
  } catch (error: unknown) {
    throw new Error(`An unexpected error occurred, ${error}`);
  }
};

export default axiosInstance;
