import { useEffect } from 'react';

export default function News() {
  useEffect(() => {
    // Динамически изменяем заголовок страницы
    document.title = 'Кузница Победы – Новости';
  }, []);
  return (
    <div className="h-screen flex items-center justify-center bg-gray-900 text-white">
      <h1 className="text-4xl font-bold">News Page</h1>
    </div>
  );
}