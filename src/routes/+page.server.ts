import { supabase } from '$lib/supabaseClient';

export async function load() {
	const { data } = await supabase.from('users').select('*');
	console.log(data);

	return {
		users: data ?? []
	};
}