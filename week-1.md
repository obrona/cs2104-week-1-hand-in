## Exercise 1

### 1.a

On Coco Montoya's album cover, the words **"Writing on the Wall" are literally written on a brick wall**. Thus, the title describes its own visual presentation—a direct pictorial self-reference.

[View the album cover](https://cocomontoya.bandcamp.com/album/writing-on-the-wall)

### 1.b

The cover shows a hand writing the word **"Magic."** Consequently, the title *Writing Magic* describes what is happening on its own cover. The sparkling pen also makes the writing appear literally magical.

[View the book](https://www.goodreads.com/book/show/136218.Writing_Magic)

### 1.c

> In English, every word can be verbed.

The noun **"verb" is itself being verbed**: it receives the past-partic ending *-ed*, producing *verbed*. The sentence therefore demonstrates its claim using the very word that names the operation.

### 1.d

Let:

- **A** be the story: "Two women walk into a bar and talk about the Bechdel-Wallace test."
- **B** be the Bechdel-Wallace test.

A refers to B by mentioning the test. B then refers back to A because the test can be applied to the story itself: it contains two women talking to each other about something other than a man. This gives the indirect cycle:

**story → Bechdel test → story**

Under variants requiring the women to be named, the story would technically fail because neither woman is named. The original/basic formulation does not always include that additional requirement.

[Bechdel-test criteria and variants](https://en.wikipedia.org/wiki/Bechdel_test#Criteria_and_variants)

### 1.e

#### 1.e.1 "This sentence no verb."

Yes. It refers directly to itself through "This sentence," and it contains no verb. It demonstrates what it says—although its lack of a verb also makes its status as a complete grammatical sentence questionable.

#### 1.e.2 "Nostalgia isn't what it used to be."

Not strictly. It does not refer to the sentence itself. It is primarily a paradoxical pun: nostalgia concerns longing for the past, while the speaker nostalgically suggests that even nostalgia was better in the past.

It could therefore be called **self-illustrating**, but not strictly self-referential.

#### 1.e.3 "Fashion is what goes out of fashion."

Yes, at the conceptual level. Fashion is defined using itself: something becomes fashion and is eventually no longer fashionable. Thus fashion includes its own disappearance in its definition. It is circular or reflexive rather than a sentence explicitly referring to itself.

#### 1.e.4 "To be or not to be."

As an isolated quotation, there is no self-reference: it concerns existence, not the sentence itself.

There is, however, a self-referential relationship when it is the title of the 1942 film *To Be or Not to Be*. The film contains a production of *Hamlet*, and the title sentence is spoken and used as a secret message inside the film. Thus, the film's title appears within the work it names.

[Plot of the 1942 film](https://en.wikipedia.org/wiki/To_Be_or_Not_to_Be_(1942_film)#Plot)

## Exercise 2

Several examples qualify:

- **Michael Ende's *The Neverending Story*** is a book involving a book. Bastian reads a book also entitled *The Neverending Story*. The boundary eventually collapses: Bastian realizes that the characters are addressing him, and he enters the story he has been reading. [Description and plot](https://en.wikipedia.org/wiki/The_Neverending_Story)

- **Shakespeare's *Hamlet*** is a play involving a play. Hamlet arranges a performance—usually called *The Mousetrap*—whose murder resembles his father's murder. He watches Claudius's reaction in order to test whether Claudius is guilty.

- **The film *Singin' in the Rain*** is a movie about making movies. Its characters are actors and filmmakers attempting to convert a silent film into a talking musical. It consequently contains several films and filmmaking scenes within the main film. [Film synopsis](https://en.wikipedia.org/wiki/Singin%27_in_the_Rain)

The supplied example, *A Midsummer Night's Dream*, also qualifies because the mechanicals perform *Pyramus and Thisbe* inside Shakespeare's play.

### Computer-science example

A classic example is a **quine**: a program that, without reading its own source file as input, prints an exact copy of its own source code.

For example, this Python quine prints itself:

```python
s = 's = %r\nprint(s %% s)'
print(s % s)
```

The program's output is the program itself, making it a computational form of direct self-reference.

[Quines in computing](https://en.wikipedia.org/wiki/Quine_(computing))

Recursion is another common example: a recursive function refers to—or calls—itself in its own definition.

## Exercise 3

The correct answer is:

**a. Yes, unquestionably. Constant vigilance!**

The word is `facetiously`.

## Exercise 4

In *The Sorcerer's Apprentice*, Mickey uses magic to automate the tedious job of carrying water. The enchanted broom follows the instruction mechanically but cannot understand Mickey's broader intention. Mickey loses control, and when he tries to destroy the broom, the attempted solution multiplies the problem.

As an analogy for LLMs and AI agents:

- The broom follows an instruction without understanding its purpose.
- Automation magnifies both useful work and mistakes.
- A poorly specified objective can produce an undesirable but superficially compliant result.
- Connecting an AI system to tools gives its errors real-world consequences.
- Stopping or correcting an autonomous process may be harder than starting it.
- Human supervision, restricted permissions, monitoring, and a reliable emergency stop are therefore important.

The crucial lesson is not simply that automation is dangerous. It is that **capability without sufficient judgment, control, and supervision can turn a small mistake into a large one**.

Paul Dukas's *The Sorcerer's Apprentice* is a symphonic poem based on Goethe's poem of the same subject; Disney used it for the Mickey Mouse sequence in *Fantasia*.

[Background on Dukas's composition](https://en.wikipedia.org/wiki/The_Sorcerer%27s_Apprentice_(Dukas))

## Exercise 6

For $i=0,\ldots,kn$, each value $0,1,\ldots,n-1$ occurs $k$ times, while $n$ occurs once. Therefore,

$$
\sum_{i=0}^{kn}\left\lfloor\frac{i}{k}\right\rfloor
=k\sum_{j=0}^{n-1}j+n
=\frac{kn(n-1)}{2}+n.
$$

### 6.a

Taking $k=2$:

$$
\sum_{i=0}^{2n}\left\lfloor\frac{i}{2}\right\rfloor
=2\frac{n(n-1)}{2}+n
=n^2.
$$

Result:

$$
\boxed{n^2}
$$

This produces the square numbers $0,1,4,9,16,\ldots$.

[OEIS A000290](https://oeis.org/A000290)

### 6.b

Taking $k=3$:

$$
\sum_{i=0}^{3n}\left\lfloor\frac{i}{3}\right\rfloor
=3\frac{n(n-1)}{2}+n
=\frac{n(3n-1)}{2}.
$$

Result:

$$
\boxed{\frac{n(3n-1)}{2}}
$$

These are the pentagonal numbers $0,1,5,12,22,\ldots$.

[OEIS A000326](https://oeis.org/A000326)

### 6.c

Taking $k=4$:

$$
\sum_{i=0}^{4n}\left\lfloor\frac{i}{4}\right\rfloor
=4\frac{n(n-1)}{2}+n
=n(2n-1).
$$

Result:

$$
\boxed{n(2n-1)}
$$

These are the hexagonal numbers $0,1,6,15,28,\ldots$.

[OEIS A000384](https://oeis.org/A000384)

### 6.d

Since

$$
\left\lfloor\frac{i}{1}\right\rfloor=i,
$$

the expression simplifies to

$$
\sum_{i=0}^{n}i
=\frac{n(n+1)}{2}.
$$

Result:

$$
\boxed{\frac{n(n+1)}{2}}
$$

These are the triangular numbers $0,1,3,6,10,\ldots$.

[OEIS A000217](https://oeis.org/A000217)

## Exercise 7

### 7.a

The result is

$$
\boxed{1}.
$$

### 7.b

There are $x+1$ terms:

$$
\sum_{i_1=0}^{x}1
=x+1.
$$

Therefore,

$$
\boxed{x+1}.
$$

### 7.c

$$
\begin{aligned}
\sum_{i_2=0}^{x}\sum_{i_1=0}^{i_2}1
&=\sum_{i_2=0}^{x}(i_2+1) \\
&=\frac{(x+1)(x+2)}{2} \\
&=\binom{x+2}{2}.
\end{aligned}
$$

Therefore,

$$
\boxed{\frac{(x+1)(x+2)}{2}=\binom{x+2}{2}}.
$$

### 7.d

The result is

$$
\boxed{\binom{x+3}{3}}
=\boxed{\frac{(x+1)(x+2)(x+3)}{6}}.
$$

### 7.e

The result is

$$
\boxed{\binom{x+4}{4}}
=\boxed{\frac{(x+1)(x+2)(x+3)(x+4)}{24}}.
$$

### 7.f

See function `ex7f` in `week-1.py`

## Exercise 10

$$
f(N) = (N + 1)!
$$

## Exercise 11

$$
f(N) = (N + 1)!
$$
