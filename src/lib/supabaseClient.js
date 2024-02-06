import { createClient } from '@supabase/supabase-js';

export const supabase = createClient(
	'https://tcicjkjjrtpxefrgyuyq.supabase.co',
	'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRjaWNqa2pqcnRweGVmcmd5dXlxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDY5MTcxNDksImV4cCI6MjAyMjQ5MzE0OX0.-hEmWaSGr1DWAs3sy347CXZHVC4fiISzdE3VmwrtGoo'
);
