import React, { useState, useEffect } from "react"; import { motion } from "framer-motion"; import { Card, CardContent } from "@/components/ui/card"; import { Button } from "@/components/ui/button"; import { Github, Linkedin, Mail, Terminal } from "lucide-react";

export default function UltimateWebsite() { const roles = [ "Cyberpunk Architect 🌌", "Hacker Mindset 💻", "Elite Developer ⚡", "3D Experience Creator 🚀", "Limitless Creator 🤯" ];

const [text, setText] = useState(""); const [index, setIndex] = useState(0); const [charIndex, setCharIndex] = useState(0);

useEffect(() => { if (charIndex < roles[index].length) { const timeout = setTimeout(() => { setText((prev) => prev + roles[index][charIndex]); setCharIndex(charIndex + 1); }, 60); return () => clearTimeout(timeout); } else { setTimeout(() => { setText(""); setCharIndex(0); setIndex((prev) => (prev + 1) % roles.length); }, 1200); } }, [charIndex, index]);

const [matrix, setMatrix] = useState([]); useEffect(() => { const interval = setInterval(() => { setMatrix(Array.from({ length: 20 }, () => Math.random().toString(36)[2])); }, 150); return () => clearInterval(interval); }, []);

return ( <div className="relative min-h-screen bg-black text-white overflow-hidden"> {/* Matrix Background */} <div className="absolute inset-0 opacity-10 text-green-500 text-xs font-mono flex flex-wrap"> {matrix.map((char, i) => ( <span key={i} className="m-1">{char}</span> ))} </div>

<div className="relative z-10 p-6">
    {/* Hero Section */}
    <motion.div
      initial={{ opacity: 0, scale: 0.9 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 1 }}
      className="text-center mb-16"
    >
      <h1 className="text-5xl md:text-7xl font-extrabold bg-gradient-to-r from-cyan-400 via-purple-500 to-pink-500 bg-clip-text text-transparent">
        KOUSHIK REDDY
      </h1>
      <h2 className="text-xl md:text-2xl text-cyan-400 mt-4 h-8">
        {text}
      </h2>
      <p className="mt-6 text-gray-400 max-w-xl mx-auto">
        Blending creativity, logic, and futuristic experiences into digital reality.
      </p>
      <div className="mt-8 flex justify-center gap-4">
        <Button className="rounded-2xl px-6 bg-cyan-500 hover:bg-cyan-400">
          Enter Dimension
        </Button>
        <Button variant="outline" className="rounded-2xl px-6 border-purple-500 text-purple-400">
          Connect
        </Button>
      </div>
    </motion.div>

    {/* 3D Tilt Cards */}
    <div className="grid md:grid-cols-3 gap-8 mb-16">
      {["Neon Stack Visualizer", "Quantum Queue Simulator", "AI Portfolio Engine"].map((project, i) => (
        <motion.div
          key={i}
          whileHover={{ rotateY: 10, rotateX: 10, scale: 1.05 }}
          transition={{ type: "spring", stiffness: 200 }}
        >
          <Card className="bg-gradient-to-br from-gray-900 to-gray-800 rounded-2xl shadow-2xl border border-purple-600">
            <CardContent className="p-6">
              <h3 className="text-xl font-bold text-cyan-400 mb-2">{project}</h3>
              <p className="text-gray-400 text-sm">
                Advanced interactive system blending logic with stunning visuals.
              </p>
            </CardContent>
          </Card>
        </motion.div>
      ))}
    </div>

    {/* Hacker Terminal Section */}
    <Card className="bg-black border border-green-500 rounded-2xl shadow-2xl mb-12">
      <CardContent className="p-6 font-mono text-green-400">
        <div className="flex items-center gap-2 mb-4">
          <Terminal size={18} /> <span>koushik@future:~$</span>
        </div>
        <p>&gt; Initializing creative engine...</p>
        <p>&gt; Loading cyber modules...</p>
        <p>&gt; Access granted ✔</p>
      </CardContent>
    </Card>

    {/* Social Section */}
    <div className="text-center space-y-4">
      <h2 className="text-2xl font-semibold text-purple-400">Connect With Me</h2>
      <div className="flex justify-center gap-6 text-cyan-400">
        <Github />
        <Linkedin />
        <Mail />
      </div>
    </div>

    <footer className="text-center text-gray-600 text-sm mt-12">
      © {new Date().getFullYear()} Koushik Reddy | Welcome to the Future 🌌
    </footer>
  </div>
</div>

); }