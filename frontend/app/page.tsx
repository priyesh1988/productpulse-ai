import { CopilotPanel } from '../components/CopilotPanel'

const metrics = [
  { label: 'Signals Ingested', value: '18.4K' },
  { label: 'Themes Clustered', value: '126' },
  { label: 'Opportunities Ranked', value: '42' },
]

export default function HomePage() {
  return (
    <main className="container">
      <section className="hero">
        <div className="muted">Product-focused GitHub starter repo</div>
        <h1 style={{ fontSize: '3rem', marginBottom: 12 }}>ProductPulse AI</h1>
        <p className="muted" style={{ maxWidth: 760, fontSize: '1.1rem' }}>
          Turn feedback, telemetry, and release signals into AI-assisted product decisions.
        </p>
      </section>

      <section className="grid grid-3">
        {metrics.map((item) => (
          <div className="card" key={item.label}>
            <div className="muted">{item.label}</div>
            <div className="metric">{item.value}</div>
          </div>
        ))}
      </section>

      <div style={{ height: 20 }} />

      <section className="grid" style={{ gridTemplateColumns: '1.2fr 0.8fr' }}>
        <div className="card">
          <h3>Why teams would use this</h3>
          <ul>
            <li>Detect recurring customer pain faster</li>
            <li>Prioritize roadmap items with transparent scoring</li>
            <li>Ask an LLM grounded in product context</li>
            <li>Bridge PM, support, engineering, and customer success</li>
          </ul>
        </div>
        <CopilotPanel />
      </section>
    </main>
  )
}
