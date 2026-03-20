'use client'

import { useState } from 'react'

export function CopilotPanel() {
  const [question, setQuestion] = useState('What are the biggest product risks right now?')
  const [answer, setAnswer] = useState('')
  const [loading, setLoading] = useState(false)

  async function askCopilot() {
    setLoading(true)
    try {
      const baseUrl = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000'
      const res = await fetch(`${baseUrl}/api/v1/copilot`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question, context: ['Recent onboarding complaints increased 22%'] }),
      })
      const data = await res.json()
      setAnswer(data.answer || JSON.stringify(data, null, 2))
    } catch (error) {
      setAnswer('Unable to contact backend.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="card">
      <h3>Product Copilot</h3>
      <p className="muted">Ask the LLM-powered product assistant for roadmap or feedback insight.</p>
      <textarea className="textarea" value={question} onChange={(e) => setQuestion(e.target.value)} />
      <div style={{ height: 12 }} />
      <button className="button" onClick={askCopilot} disabled={loading}>
        {loading ? 'Thinking...' : 'Ask Copilot'}
      </button>
      {answer && (
        <>
          <div style={{ height: 16 }} />
          <div className="card">
            <strong>Answer</strong>
            <p className="muted">{answer}</p>
          </div>
        </>
      )}
    </div>
  )
}
