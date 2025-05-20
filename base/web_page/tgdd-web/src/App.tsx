import { useEffect, useState } from 'react'
import './App.css'
import type { Product } from './types/ProductTypes'
import { ProductGrid } from './components/product/ProductGrid'
import { getAllProducts, searchProducts, getProductsByCategory } from './api/productService'

function App() {
  const [products, setProducts] = useState<Record<string, Product>>({})
  const [loading, setLoading] = useState(false)
  const [searchQuery, setSearchQuery] = useState('')
  const [selectedCategory, setSelectedCategory] = useState('all')

  const toProductRecord = (data: Product[]): Record<string, Product> => {
    return data.reduce((acc, product) => {
      acc[product.product_name] = product
      return acc
    }, {} as Record<string, Product>)
  }

  const fetchAll = async () => {
    setLoading(true)
    try {
      const data = await getAllProducts()
      setProducts(toProductRecord(data))
    } catch (error) {
      console.error('Error fetching products:', error)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchAll()
  }, [])

  const handleSearch = async (query: string) => {
    setSearchQuery(query)
    if (!query.trim()) {
      fetchAll()
      return
    }

    setLoading(true)
    try {
      const data = await searchProducts(query)
      setProducts(toProductRecord(data))
    } catch (error) {
      console.error('Error searching products:', error)
    } finally {
      setLoading(false)
    }
  }

  const handleCategoryChange = async (category: string) => {
    setSelectedCategory(category)
    setLoading(true)
    try {
      let data: Product[]
      if (category === 'all') {
        data = await getAllProducts()
      } else {
        data = await getProductsByCategory(category)
      }
      setProducts(toProductRecord(data))
    } catch (error) {
      console.error('Error fetching category products:', error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <>
      <header className='bg-white shadow-md py-6 mb-6'>
        <div className='container mx-auto px-4 text-center'>
          <h1 className='text-3xl font-extrabold text-gray-800'>Thái Bảo Tráng Dương</h1>
          <p className='text-lg text-gray-600 mt-2'>Diệt trừ cái ác, bảo vệ thế giới</p>
        </div>
      </header>

      <main className='mx-auto px-4 pb-8'>
        <div className='bg-white p-4 rounded-lg mb-6'>
          <div className='flex flex-col gap-4'>
            <div className='flex justify-between items-center'>
              <h2 className='text-lg font-semibold'>Danh sách sản phẩm</h2>
              <div className='flex gap-4'>
                <select className='border rounded px-2 py-1 text-sm'>
                  <option>Giá thấp đến cao</option>
                  <option>Giá cao đến thấp</option>
                </select>
              </div>
            </div>

            <div className='flex gap-4'>
              <input
                type='text' placeholder='Tìm kiếm sản phẩm...'
                className='flex-1 border rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500'
                value={searchQuery}
                onChange={(e) => handleSearch(e.target.value)}
              />
              <select
                className='border rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500'
                value={selectedCategory}
                onChange={(e) => handleCategoryChange(e.target.value)}
              >
                <option value='all'>Tất cả</option>
                <option value='Mobile Phone'>Điện thoại</option>
                <option value='Laptop'>Laptop</option>
              </select>
            </div>
          </div>
        </div>

        {loading ? (
          <div className='text-center py-12'>
            <div className='inline-block animate-spin h-8 w-8 border-4 border-gray-300 border-t-blue-500 rounded-full'></div>
            <p className='mt-4 text-gray-600'>Loading products...</p>
          </div>
        ) : (
          <div className='slideUp'>
            <ProductGrid products={products} />
          </div>
        )}
      </main>

      <footer className='bg-white border-t border-gray-200 py-6 mt-12'>
        <div className='container mx-auto px-4 text-center text-gray-500 text-sm'>
          <p>© 2025 Thái Bảo Tráng Dương. All rights reserved.</p>
        </div>
      </footer>
    </>
  )
}

export default App
