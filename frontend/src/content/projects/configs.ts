import { defineCollection, z } from "astro:content";

const projects = defineCollection({
  projects: {
    schema: z.object({
      title: z.string(),
      description: z.string(),
      tags: z.array(z.string()),
      image: z.string(),
      url: z.string().url().optional(),
    }),
  },
});

export const collections = { projects };
