# TypeScript Frontend Learning

TypeScript fundamentals and practice problems.

## Structure

- **`01-fundamentals/`** - Core TypeScript concepts
  - `01-basics.ts` - Basic types and primitives
  - `02-main.ts` - Main TypeScript concepts
  - `03-functions.ts` - Function types and signatures

- **`02-practice/`** - Practice exercises
  - `practice.ts` - TypeScript exercises

- **`build/`** - Compiled JavaScript output
  - `*.js` - Compiled files

## How to Use

### Prerequisites

- Node.js 16+
- TypeScript installed

### Compilation

```bash
# Compile all TypeScript files
tsc

# Watch mode (auto-compile on changes)
tsc --watch
```

### Running Files

```bash
# After compilation, run with Node
node build/01-basics.js
```

## Topics Covered

### Fundamentals

#### 01-basics.ts
- Primitive types (string, number, boolean, null, undefined)
- Non-primitive types (object, array, function)
- Type annotations
- Const, let, var declarations

#### 02-main.ts
- Main TypeScript concepts overview
- Type system fundamentals
- Common patterns

#### 03-functions.ts
- Function type annotations
- Function signatures
- Return types
- Optional and default parameters

### Practice

- `practice.ts` - Hands-on TypeScript exercises

## Learning Path

1. Start with `01-basics.ts` to understand type system
2. Move to `02-main.ts` for comprehensive concepts
3. Study `03-functions.ts` for type-safe functions
4. Practice with `practice.ts`
5. Compile and run to verify understanding

