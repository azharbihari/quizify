export interface Subject {
    id: number;
    name: string;
    topics: Topic[];
}

export interface Topic {
    id: number;
    name: string;
    subject: Subject;
}

export interface Difficulty {
    value: string;
    label: string;
}

export interface Choice {
    id: number;
    question: Question;
    text: string;
    is_correct: boolean;
    created_at: Date;
    updated_at: Date;
}

export interface Question {
    id: number;
    text: string;
    slug: string;
    difficulty: string;
    duration: number;
    subject: Subject;
    topic: Topic;
    created_at: Date;
    updated_at: Date;
    choices: Choice[];
}

export interface Quiz {
    [x: string]: string;
    id: number;
    name: string;
    user: number;
    slug: string;
    subject: Subject;
    topic: Topic;
    number_of_questions: number,
    difficulty: string;
    questions: Question[];
    answers: Choice[];
    score: number | null;
    created_at: Date;
    updated_at: Date;
    status: string;
    duration: number;
}

export interface Token {
    access_token: string;
    refresh_token: string;
}


export interface User {
    email: string;
    password: string;
    first_name: string;
    last_name: string;
}