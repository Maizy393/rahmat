import Image from "next/image";
import styles from "./page.module.css";
import Link from "next/link";
interface Employers {
    id: number
    name: string
    icon: string
    ref: string
    tags: string[]
}
const data = await fetch("http://127.0.0.1:8080/employers");
const employers: Employers[] = await data.json();

export default function HomePage() {
    return (
        <div className={styles.container}>
            <h1 className={styles.pageTitle}>Заказчики</h1>
            <div className={styles.grid}>
                {employers.map(c => {
                    const classes = [styles.card]
                    if (c.name === 'Uber')   classes.push(styles.uberCard)
                    if (c.name === 'Tesla')  classes.push(styles.teslaCard)
                    return (
                        <Link
                            key={c.id}
                            href={c.ref}
                            target="_blank"
                            rel="noopener noreferrer"
                            className={classes.join(' ')}
                        >
                            <div className={styles.iconBox}>
                                <img src={c.icon} alt={c.name} className={styles.icon} />
                            </div>
                            <h3 className={styles.title}>{c.name}</h3>
                            <div className={styles.tags}>
                                {c.tags.map((t, i) => (
                                    <span key={i} className={styles.tag}>{t}</span>
                                ))}
                            </div>
                        </Link>
                    )
                })}
            </div>
        </div>
    )
}