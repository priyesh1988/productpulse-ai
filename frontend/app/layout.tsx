import './globals.css'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'ProductPulse AI',
  description: 'AI-native product operating system',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
