import { useEffect } from 'react';

export default function HelpUs() {
  useEffect(() => {
    // Динамически изменяем заголовок страницы
    document.title = 'Кузница Победы – Поддержать нас';
  }, []);
  return (
    <div className="h-screen flex items-center justify-center bg-gray-900 text-white">
      <h1 className="text-4xl font-bold">Help Us Page</h1>
    </div>
  );
}