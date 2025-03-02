import { useEffect } from 'react';

export default function Contact() {
  useEffect(() => {
    // Динамически изменяем заголовок страницы
    document.title = 'Кузница Победы – Инструкции по плетению';
  }, []);
  return (
    <div className="h-screen flex items-center justify-center bg-gray-900 text-white">
      <h1 className="text-4xl font-bold">Instructions Page</h1>
    </div>
  );
}