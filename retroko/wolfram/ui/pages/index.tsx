// pages/index.tsx
import Head from 'next/head';
import RetrokoWolframUI from '../../components/RetrokoWolframUI©

export default function Home() {
  return (
    <>
      <Head>
        <title>RETROKO → Wolfram</title>
      </Head>
      <main className="min-h-screen bg-gray-100 py-12">
        <RetrokoWolframUI />
      </main>
    </>
  );
}