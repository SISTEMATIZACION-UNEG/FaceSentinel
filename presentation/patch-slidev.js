// Script de compatibilidad para rutas de Windows con espacios en Slidev
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const cliDistDir = path.join(__dirname, 'node_modules', '@slidev', 'cli', 'dist');

if (fs.existsSync(cliDistDir)) {
  const files = fs.readdirSync(cliDistDir);
  for (const file of files) {
    if (file.endsWith('.js')) {
      const filePath = path.join(cliDistDir, file);
      let content = fs.readFileSync(filePath, 'utf-8');
      const target = 'main.replace("__ENTRY__", baseInDev + encodeURI(toAtFS(join(clientRoot, "main.ts"))))';
      const replacement = 'main.replace("__ENTRY__", baseInDev + (mode === "dev" ? encodeURI(toAtFS(join(clientRoot, "main.ts"))) : toAtFS(join(clientRoot, "main.ts"))))';
      if (content.includes(target)) {
        content = content.replace(target, replacement);
        fs.writeFileSync(filePath, content, 'utf-8');
        console.log(`[Slidev Patch] Aplicado parche de compatibilidad en ${file}`);
      }
    }
  }
}
